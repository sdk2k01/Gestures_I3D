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
- [About Issues](#About-Issues)
  - [Creating an Issue](#Creating-an-Issue)
    - [Creating an Issue from a Repository](#Creating-an-Issue-from-a-Repository)
    - [Creating an Issue from a Comment](#Creating-an-Issue-from-a-Comment) 
  - [Linking a Pull Request to an Issue](#Linking-a-Pull-Request-to-an-Issue)


## Contributing to Gestures_I3D
We appreciate your interest in contributing to Gestures_I3D. It's crucial to inform the team of your desire to contribute before you start developing code, depending on the sort of contribution:

1. You intend to propose and use a new feature..
    - Post about your intended feature in an [issue](https://github.com/sdk2k01/Gestures_I3D/issues),
    and we shall discuss the design and implementation. Once we agree that the plan looks good, go ahead and implement it.
2. You want to implement a feature or bug-fix for an outstanding issue.
    - Search for your _issue_ in the [issue list](https://github.com/sdk2k01/Gestures_I3D/issues).
    - Pick an issue and comment that you'd like to work on the feature or bug-fix.

Once you implement and test your feature or bug-fix, please submit a Pull Request to [Gestures_I3D](https://github.com/sdk2k01/Gestures_I3D).

## Developing Gestures_I3D
### Prerequisites

- <img src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png" height="22"> Python 3.6 or above ( ideally Python 3.10+ )
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Cmake.svg/1200px-Cmake.svg.png" height="22"> CMake

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
3. Click __Pull Request__.
4. Use the _base_ branch dropdown menu to select the branch you'd like to merge your changes into, then use the _compare_ branch drop-down menu to choose the topic branch you made your changes in.
5. Type a Title and Description for your Pull Request.
6. To create a pull request that is ready for review, click __Create Pull Request__. To create a draft pull request, use the drop-down and select __Create Draft Pull Request__, then click __Draft Pull Request__.

### Describe a Pull Request
1. Use the format specified in pull request template for the repository. __Populate the stencil completely__ for maximum verbosity.
   - Tag the actual issue number by replacing `#[issue_number]`, e.g. `#42`. This closes the issue when your PR is merged.
   - Tag the actual issue author by replacing `@[author]`, e.g. `@issue_author`. This brings the reporter of the issue into the conversation.
   - Mark the tasks off your checklist by adding an `x` in the `[ ]` e.g. `[x]`. This checks off the boxes in your to-do list.
2. Describe your change in detail. Too much detail is better than too little.
   - Such as how you tested your change, the bugs fixed (if any) and the functionalities added.
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

## About Issues
Please read this if you are unfamiliar in handling _Issues_. 
### Creating an Issue
Issues can be created in a variety of ways, so you can choose the most convenient method for your workflow.
#### Creating an Issue from a Repository
1. Navigate to the main page of the repository.
2. Under your repository name, click __Issues__.
3. Click __New issue__.
4. If your repository uses issue templates, click __Get started__ next to the type of issue you'd like to open. Or, click __Open a blank issue__ if the type of issue you'd like to open isn't included in the available options.
5. Type a title and description for your issue.
6. When you're finished, click __Submit new issue__.
#### Creating an Issue from a Comment
You can open a new issue from a comment in an issue or pull request. When you open an issue from a comment, the issue contains a snippet showing where the comment was originally posted.
1. Navigate to the comment that you would like to open an issue from.
2. In that comment, click __⋯__ .
3. Click __Reference in new issue__.
4. Use the "Repository" drop-down menu, and select the repository you want to open the issue in.
5. Type a title and description for your issue.
6. Click __Create issue__.
7. When you're finished, click __Submit new issue__.
### Linking a Pull Request to an Issue
To indicate that work is in progress, you can link an issue to a pull request. When the pull request merges, the linked issue automatically closes.
1. Navigate to the main page of the repository.
2. Under your repository name, click __Pull Request__.
3. In the list of pull requests, click the pull request that you'd like to link to an issue.
4. In the right sidebar, in the _Development_ section click.
5. Click the issue you want to link to the pull request.