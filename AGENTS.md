# Repository Guidelines

## Project Structure

This repository is currently empty. Keep application code in `src/`, automated checks in `tests/`, and static files in `assets/` if and when they are introduced. Avoid placing generated output, local environment files, or credentials in version control.

## Build, Test, and Development

No build system, package manifest, or test runner is configured yet. When adding one, document the supported commands here and in `README.md`. Prefer the project’s native commands, for example:

```sh
npm run dev    # run the local development server
npm test       # run the automated test suite
npm run build  # create a production build
```

Do not add dependencies or tooling unless the implementation requires them.

## Coding Style and Naming

Match the conventions of the language and tooling introduced with the project. Use descriptive names: `user-profile.ts`, `calculateTotal`, and `UserProfile` are preferred over abbreviations. Keep files focused, favor small native-language helpers over new abstractions, and configure a formatter or linter when the first supported language needs one.

## Testing

Add tests alongside each non-trivial behavior in `tests/` or in the language’s established test location. Name test files after the unit under test, such as `tests/calculate-total.test.ts`. Run the full test command before opening a pull request. Add regression coverage for bug fixes.

## Commits and Pull Requests

There is no Git history yet, so no commit convention is established. Use concise imperative subjects, such as `feat: add invoice totals` or `fix: handle empty input`. Keep commits focused. Pull requests should explain the change, link relevant issues, list validation performed, and include screenshots for visible UI changes.

## Security and Configuration

Never commit secrets. Store local settings in ignored environment files (for example, `.env.local`) and provide a sanitized `.env.example` whenever configuration becomes necessary.
