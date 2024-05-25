# How to Keep Your Fork Updated with the Original Repository

## Steps to Work on a Cloned Repository and Keep It Updated with the Original Repository

1. **Clone the Repository:**
   First, clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/aousabdo/phidata.git
   ```

2. **Add the Original Repository as a Remote:**
   Add the original repository (often referred to as the "upstream" repository) as a remote to your local repository. This allows you to pull updates from the original repository. Use the following commands:
   ```bash
   cd phidata
   git remote add upstream https://github.com/phidata/phidata.git
   ```

3. **Verify the Remotes:**
   Verify that the new remote has been added correctly by using the following command:
   ```bash
   git remote -v
   ```

   You should see output similar to this:
   ```
   origin    https://github.com/aousabdo/phidata.git (fetch)
   origin    https://github.com/aousabdo/phidata.git (push)
   upstream  https://github.com/phidata/phidata.git (fetch)
   upstream  https://github.com/phidata/phidata.git (push)
   ```

4. **Fetch Updates from Upstream:**
   Fetch updates from the upstream repository to ensure you have the latest changes. Use the following command:
   ```bash
   git fetch upstream
   ```

5. **Merge Updates into Your Local Branch:**
   Merge the fetched updates into your local branch. Assuming you are working on the `main` branch, use the following commands:
   ```bash
   git checkout main
   git merge upstream/main
   ```

6. **Resolve Conflicts:**
   If there are any merge conflicts, Git will notify you. Resolve the conflicts in your preferred text editor, then add the resolved files and commit the merge:
   ```bash
   git add <resolved_file>
   git commit
   ```

7. **Push Changes to Your Fork:**
   After merging the updates from the upstream repository, you can push the changes to your forked repository on GitHub:
   ```bash
   git push origin main
   ```

By following these steps, you can keep your local repository up to date with changes from the original repository while working on your forked version.
