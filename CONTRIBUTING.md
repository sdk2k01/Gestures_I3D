# Table of Contents
- [Contributing to Gestures_I3D](#contributing-to-Gestures_I3D)
- [Developing Gestures_I3D](#developing-Gestures_I3D)
  - [Prerequisites](#prerequisites)
  - [Committing Changes in Local Repository](#Committing-Changes-in-Local-Repository)
- [Pull Request Guidelines](#Pull-Request-Guidelines)
  - [Creating a Pull Request](#Creating-a-Pull-Request)
  - [Describe a Pull Request](#Describe-a-Pull-Request)
  - [Request Review](#Request-Review)
  - [Incorporating Feedback](#Incorporating-Feedback)



## Contributing to Gestures_I3D
We appreciate your interest in contributing to Gestures_I3D. It's crucial to inform the team of your desire to contribute before you start developing code, depending on the sort of contribution:

1. You intend to propose and use a new feature..
    - Post about your intended feature in an [issue](https://github.com/sdk2k01/Gestures_I3D/issues),
    and we shall discuss the design and implementation. Once we agree that the plan looks good, go ahead and implement it.
2. You want to implement a feature or bug-fix for an outstanding issue.
    - Search for your _issue_ in the [issue list](https://github.com/sdk2k01/Gestures_I3D/issues).
    - Pick an issue and comment that you'd like to work on the feature or bug-fix.

Once you implement and test your feature or bug-fix, please submit a Pull Request to https://github.com/sdk2k01/Gestures_I3D.

## Developing Gestures_I3D
### Prerequisites
- Python 3.6 or above ( ideally Python 3.10+ )
- CMake

### Committing Changes in Local Repository
1. Switch to a new branch ( ex - `Feature` ), if you are working on a new feature or fixing a bug.
 - `zsh` / `bash` / `git-bash`

```zsh
git checkout -b <branch_name>
```
2. Create an isolated virtual environment as described in the project's [README](https://github.com/sdk2k01/Gestures_I3D/blob/main/README.md) section.
3. Activate the virtual environment:
 - `zsh` or `bash`

```zsh
source ./venv/bin/activate
```
4. Make all desired changes and stage them.
 - `zsh` / `bash` / `git-bash`
```zsh
git add <changed_file_or_directory_name>
```
5. Install `pre-commit`.
 - `zsh` / `bash` / `git-bash`
```zsh
pip install pre-commit
```
* Follow the other steps to set-up or modify the pre-commit hooks as specified in the [official pre-commit documentation.](https://pre-commit.com/)
6. Install the pre-commit hooks:
 - `zsh` / `bash` / `git-bash`
```zsh
pre-commit install
```
7. Run `pre-commit` on the staged files.
 - `zsh` / `bash` / `git-bash`
```zsh
pre-commit
```
* Re-formatted files would need to be staged again, as specified in step 4.
8. Once all the files to be committed are staged, commit your changes providing a suitable and self-explanatory commit message.
 - `zsh` / `bash` / `git-bash`
```zsh
git commit -m "<commit_message>"
```
## Pull Request Guidelines
Please read this documentation if you are unfamiliar with pull requests. Following these guidelines will speed up the process of adding your code to the repository.
### Creating a Pull Request
1. Navigate to the main page of the repository.
2. In the __Branch__ menu, choose the branch that contains your commits.
3. Click Pull Request
4. Use the _base_ branch dropdown menu to select the branch you'd like to merge your changes into, then use the _compare_ branch drop-down menu to choose the topic branch you made your changes in.
5. Type a Title and Description for your Pull Request.
6. To create a pull request that is ready for review, click __Create Pull Request__. To create a draft pull request, use the drop-down and select __Create Draft Pull Request__, then click __Draft Pull Request__.

### Describe a Pull Request
1. Use the format specified in pull request template for the repository. __Populate the stencil completely__ for maximum verbosity.
   - Tag the actual issue number by replacing `#[issue_number]`, e.g. `#42`. This closes the issue when your PR is merged.
   - Tag the actual issue author by replacing `@[author]`, e.g. `@issue_author`. This brings the reporter of the issue into the conversation.
   - Mark the tasks off your checklist by adding an `x` in the `[ ]` e.g. `[x]`. This checks off the boxes in your to-do list. The more boxes you check, the better.
2. Describe your change in detail. Too much detail is better than too little.
3. Describe how you tested your change, the bugs it fixed (if any) and the functionality it adds.
4. Add images with appropriate captions to show examples of the new version of the code working.
5. Check the Preview tab to make sure the Markdown is correctly rendered and that all tags and references are linked. If not, go back and edit the Markdown.

![This is an image](https://opensource.creativecommons.org/contributing-code/pr-guidelines/populated_pr.png)
### Request Review
1. Once your PR is ready, __remove the__ `[WIP]` __from the title__ and/or change it from a draft PR to a regular PR.
2. If a specific reviewer is not assigned automatically, please request a review from the project maintainer and any other interested parties manually.
### Incorporating Feedback
1. If your PR gets a 'Changes requested' review, you will need to address the feedback and update your PR by pushing to the same branch. You don't need to close the PR and open a new one.
2. Be sure to re-request review once you have made changes after a code review.
![This is an image](https://opensource.creativecommons.org/contributing-code/pr-guidelines/rereview.png)
3. Asking for a re-review makes it clear that you addressed the changes that were requested and that it's waiting on the maintainers instead of the other way round.
![This is an image](https://opensource.creativecommons.org/contributing-code/pr-guidelines/difference.png)