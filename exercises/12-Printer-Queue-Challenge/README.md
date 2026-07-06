## 12 - Printer Queue Challenge

Create a printer queue with priorities.

Class `PrintQueue`:

- `add_job(name, pages, priority)`
- `next_job()` processes and returns the next job (name)
- `pending_pages()` returns total pending pages

Priority rule: smaller number = higher priority.
If priorities tie, keep insertion order.

## Required variables

- `printer`: instance of `PrintQueue`
- `processed`: list with 3 processed jobs
- `pages_left`: pending pages at the end
