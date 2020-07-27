# How to add terms to this repository

![](https://img.shields.io/badge/-status:wip-5319e7.svg)

In this tutorial, we will use VS Code but if you prefer, you can use any other editor or even command line tools.

1. Clone the repository.

   - Bring up the Command Palette (<kbd>command</kbd> <kbd>shift</kbd> <kbd>P</kbd>)
   
   - Type `git clone`
   
   - When asked to provide repository URL, paste `https://github.com/DHRI-Curriculum/glossary/` into the box.
   
   - VS Code will ask you where to save your local clone of the repository. Choose wherever you would like to have it.
   
   - When asked "Would you like to open the cloned repository?", press "Open in New Window" (to ensure no conflict with any other windows you may have open).

2. Create your own branch.
   
   - Click the branch name that you are currently on (likely "master") in the lower-left corner
      ![](../images/choose-branch.png)

   - Select "Create new branch from..."
      ![](../images/create-new-branch-from.png)
   
   - Provide a branch name for your new branch (something like `<your-username>-suggested-terms`) followed by <kbd>enter</kbd>
      ![](../images/new-branch-name.png)
   
   - When asked to "Select a ref to create" your branch, select `origin/v2.0`
      ![](../images/select-a-ref.png)
   
   - You should now be on your own branch of this repository. You can verify that you're on the correct branch by checking your lower-left corner that should have your branch name instead of the formerly active branch.
      ![](../images/your-branch-is-active.png)

3. Add whichever term(s) you think should be added to the `terms` folder:

   - Each term should be in a separate `<term>.md` file. Keep the filename lowercase.
   
   - Add the term as the first header in the file (`# <term>`)
   
   - In the first paragraph after the first header, add the explanation of the term.
   
   - (Optional) Add a section `## Readings` where you add a bulletpoint for each _reading_ you think is valuable to grasp the term that you want to add to the glossary.
   
   - (Optional) Add a section `## Tutorials` where you add a bulletpoint for each _tutorial_ you think is valuable to grasp the term that you want to add to the glossary.
   
   - (If you want a model file to look at, [here is one available](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/model.md).)
   
4. Add a pull request to the `v2.0` branch.
