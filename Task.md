# Review + Completion Checklist

## PR Review Summary

### Review comments

1. Accessibility has been implemented correctly in [app/static/index.html](app/static/index.html). The page now declares a language, includes a descriptive title, adds proper image alt text, uses a real `main` landmark, correct heading hierarchy, real form labels, and an actual submit button. These are important keyboard and screen-reader improvements and are aligned with WCAG expectations.
2. Performance is improved without changing the page structure in a risky way. In [app/static/index.html](app/static/index.html), the script is deferred and the images include widths, heights, and lazy loading, which helps reduce render-blocking and cumulative layout shift.
3. The CI workflow in [.github/workflows/ci.yml](.github/workflows/ci.yml) is set up correctly: it triggers on pushes and pull requests to `main`, installs dependencies from `requirements.txt`, and runs the full `pytest` suite. This gives the team automatic regression protection for future changes.

### Verdict

Approved — no blocking issues found. The PR meets the lab requirements, passes the project tests, and is ready to merge.

---

## Completed Task Checklist

### Part A — Accessible & fast front end

- [x] TASK 1 — Perceivable: language, descriptive title, and image alt text added.
- [x] TASK 2 — Structure & controls: `main` landmark added, heading hierarchy corrected, fake button replaced with a real `<button>`.
- [x] TASK 3 — Labels: real `<label for="...">` elements tied to correct inputs.
- [x] TASK 4 — Contrast: darkened text and brand colors to meet WCAG AA contrast.
- [x] TASK 5 — Performance: script deferred; image dimensions added; main content image set to lazy load.

### Part B — CI pipeline

- [x] TASK 6 — Workflow triggers added for `push` and `pull_request` on `main`.
- [x] TASK 7 — Test job added to install dependencies and run `pytest` on `ubuntu-latest`.

### Part C — Ship & review

- [x] PR branch created and changes pushed.
- [x] CI pipeline checked and passing.
- [x] Peer review completed with approval verdict.

---

## Reflection

The accessibility change that a sighted mouse user would not notice but a keyboard or screen-reader user depends on is the correct form labeling and real button semantics. Without proper labels and controls, assistive technology cannot reliably announce what each field is or how to activate actions, even though the page may look normal to a sighted user. Automating the accessibility and performance checks in CI stops a teammate from accidentally shipping an inaccessible or slow page later because the pipeline fails before that code reaches production, which creates a safety net for the whole team.
