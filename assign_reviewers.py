import os
import gitlab
import datetime
import random

INTERVAL = datetime.timedelta(days=7)
TARGET_REVIEWERS = 2
LECTURER_ID = 17495
LECTURER_USERNAME = "f.dahms"

now = datetime.datetime.now()
last_release = now - INTERVAL
print(f"ReviewBot runs on {now.isoformat()}")


# Gitlab connection
gl = gitlab.Gitlab(url="https://gitlab.rlp.net", private_token=os.environ["ACCESS_TOKEN"])
# gl.enable_debug()
project = gl.projects.get(os.environ["CI_PROJECT_PATH"])


print("Closing old merge requests")
for mr in project.mergerequests.list(iterator=True,
            query_parameters={"state": "opened", "created_before": last_release.isoformat()}):

    author_name = mr.author["name"]
    print(f"  Closing MR {mr.id} '{mr.title}' by '{author_name}' created on {mr.created_at}")
    mr.state_event = "close"
    mr.save()

print("Assigning Reviewers")

print("  Collecting relevant MRs")
merge_requests = {}
for mr in project.mergerequests.list(iterator=True,
            query_parameters={"state": "opened", "created_after": last_release.isoformat()}):

    author_id = mr.author["id"]
    author_name = mr.author["name"]

    if author_id in merge_requests:
        current_updated = datetime.datetime.fromisoformat(mr.updated_at)
        other_updated = datetime.datetime.fromisoformat(merge_requests[author_id].updated_at)

        print(f"    Duplicate MR by {author_name} (id: {author_id}) - last updated: {current_updated} vs {other_updated}")
        if current_updated > other_updated:
            merge_requests[author_id] = mr
    else:
        merge_requests[author_id] = mr

print(f"  Collected a total of {len(merge_requests)} submissions")

def mutex_derangements(n, m):
    if m >= n:
        return None

    has_fixpoint = True

    while has_fixpoint:
        result = []
        for _ in range(m):
            l = list(range(n))
            random.shuffle(l)
            result.append(l)

        has_fixpoint = False
        for i in range(n):
            s = set([i])
            for r in result:
                s.add(r[i])
            if len(s) < m + 1:
                has_fixpoint = True
                break

    return result

n_reviewers = min(TARGET_REVIEWERS, len(merge_requests)-1)

if len(merge_requests) > 0:
    review_permutation = mutex_derangements(len(merge_requests), n_reviewers)
    authors = list(merge_requests.keys())

    for i in range(len(merge_requests)):
        mr = merge_requests[authors[i]]
        author_name = mr.author["name"]

        reviewer_ids = []
        reviewer_names = []
        for reviewer_idx in [p[i] for p in review_permutation]:
            reviewer_id = authors[reviewer_idx]
            reviewer_ids.append(reviewer_id)

            reviewer_username = merge_requests[reviewer_id].author["username"]
            reviewer_names.append(merge_requests[reviewer_id].author["name"])

            mr.notes.create({"body": f"Bitte reviewen @{reviewer_username}"})

        if n_reviewers < TARGET_REVIEWERS:
            mr.notes.create({"body": f"Bitte reviewen @{LECTURER_USERNAME}"})
            reviewer_names.append("LECTURER")
            if LECTURER_ID not in reviewer_ids:
                reviewer_ids.append(LECTURER_ID)

        reviewer_list = " and ".join(reviewer_names)
        print(f"Set reviewers of MR {mr.id}: '{mr.title}' by {author_name} to be: {reviewer_list}")

        mr.reviewer_ids = reviewer_ids
        mr.save()

else:
    print("No submissions. No reviewers assigned.")
