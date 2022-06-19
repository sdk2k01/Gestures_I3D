# Contributing to this project

## Pre-Requisites

- Python 3.6 or above ( ideally python3.10+ )
- CMake

## Committing Changes

1. Switch to a new branch ( ex - `Feature` ), if you are working on a new feature or fixing a bug.
 - `zsh` / `bash` / `git-bash`

```zsh
git checkout -b <branch_name>
```

2. Create an isolated virtual environment as described in the project's README section.

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
