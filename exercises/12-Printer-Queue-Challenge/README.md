## 12 - Printer Queue Challenge

## What you will learn

In this final challenge you will combine queue logic, priorities, and totals.
You will simulate a printer workflow closer to a real use case.

## What you need to implement

Create a `PrintQueue` class with:

- `add_job(name, pages, priority)`
- `next_job()` processes and returns next job name
- `pending_pages()` returns total pending pages

Rules:

- Smaller priority number means more urgent.
- If two jobs share priority, keep insertion order.

## Step-by-step guide

1. Represent each job with name, pages, and priority.
2. In `add_job`, insert while preserving priority order.
3. For ties, place new job after existing jobs with same priority.
4. In `next_job`, process and return next job name.
5. If queue is empty, `next_job()` returns `None`.
6. In `pending_pages`, sum pages of pending jobs.
7. Create `printer`, process 3 jobs, and store names in `processed`.
8. Store final pending pages in `pages_left`.

## Quick example

If you add jobs with priorities 3, 1, and 2:

- Priority 1 job runs first.
- Then priority 2.
- Then priority 3.

## Note

This challenge checks both priority ordering and consistency of pending-page tracking.

## Required variables

- `printer`: instance of `PrintQueue`
- `processed`: list with 3 processed jobs
- `pages_left`: pending pages at the end
