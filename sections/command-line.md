# Command Line

## Commands 
[Note that these commands are Unix Code]

`pwd` - show the current (or "working") directory. Stands for "print working directory"

`ls` - show the files and folders in the working directory. I think of it as standing for "list stuff," but it's probably just short for "list."

- `ls -1` - show the files and folders in a nice vertical column.

`cd` - move to a directory, i.e. `cd Desktop` will move to the "Desktop" folder. Some special cases:

- `cd ..` - go to the directory above
- `cd ~` go to your "home" directory, i.e. /Users/<yourname>
- `cd` (by itself) also goes to the home directory
- `cd -` go to the last directory you were in before the current
- `cd ../..` travel two directories up
- `cd Documents/thesis-drafts` move two directories, from the home folder to "thesis-drafts," skipping "Documents"

`touch <filename>` - Create an empty text file named <filename> in your current directory.

`code <filename>` - Open file in VS Code (and create it, if it does not already exist).

`mkdir <folder name>` - Create a directory named `<folder name>` in the current working directory.

`echo <some text>` - Print out any text you give it. Often used with a redirect to add text to a file.

`cat <filename>` - Print the contents of a file to the screen, in this case the contents of `<filename>`

`>` - Redirects printed output to a text file, as in `echo "this is some text" > hello.txt`

`>>` - Redirect and append. If there's already a file with text in it, this command will add that text to the file without destroying and recreating it.

`|` - Pipe symbol. Takes output from one command and uses it as input for another command.

`less <filename>` - Print out the contents of a file in a paginated form. Use `<Control-v>` and `<Alt-v>` (or `<Command-v` and `<Option-v>`) to move up and down. Press `q` to quit.

`head <filename>` - Print the first section of a file

`tail <filename>` - Print the last section of a file

`wc -l` - Takes input and returns the number of lines in that input, as in `cat <filename> | wc -l`

`sort` - Arrange lines in a file in numeric and alphabetical order.

`uniq` - Remove duplicate lines from input, as in `cat <filename> | uniq`. To show the duplicate files, use `uniq -d`. Often most useful after using `sort`, since it only removed duplicates that are next to one another.

`mv` - Move or rename a file. For example, `mv file1 file2` will rename `file` to `file2`. You can also specify another destination, so that `mv file1 ~` will move file1 to the home folder without renaming it.

`rm <filename>` - Permanently remove a file from your computer.


Also check out [other useful commands](other-commands.md)

## Glossary

### Synonyms for the command line

*bash* - the programming language used in the command line. (Yes, we tricked you, you're already programming!) Short for "Born Again SHell," for reasons people on the internet will happily tell you about.

*the terminal* - Particularly used to refer to the command line on OSX. This term made more sense when universities used mainframes and every computer was only a terminal.

*the shell* - The part of an operating system that interacts with a human. Technically, anything you do in a graphical interface is also in a shell, but in practice this is just another synonym for the command line.

*cli* - "Command Language Interpreter," this is a super technical term for the command line used to impress everyone around you.

### Other Terms

*GUI* - "Graphical User Interface." Pronounced "gooey," like delicious gooey chocolate. Basically, anything on a computer that isn't in the command line. All familiar elements of day-to-day computer tasks such as images, windows, prompts, buttons, and progress bars are part of the GUI. The way most people interact with computers. Some tasks can only be done in a GUI, while others can only be done in the command line.

*root* - A word for the administrative user on a system. You often need administrative privileges to install programs or access certain system folders using the command line. You can tell you're root when your `$` prompt turns into a `#` prompt. To become root, type `su` and enter the password you use to log in. (No characters or asterisks will appear, just type your password and press enter.) You can also run a single command as root by typing `sudo` before the command.

*UNIX* - A family of operating systems that have a multi-user model and a particular design philosophy. Both OSX and Linux are UNIXes. Windows is not.

*REPL* - "Read Eval Print Loop" The process of typing something in to the command line and getting something back out. Like most things to do with the command line, not as complicated (or scary) as it sounds.

*Text editor* - A program for creating and editing plain text files. Unlike word processors such as LibreOffice and Word, which create complex documents in the form of archives that include formatting information and other metadata, a plain text editor creates a single file. Programmers tend to use plain text files because computers can work with them easily. Sublime Text, Nano, and VI are examples of text editors.

*path* - A list of folders on your system that are checked for programs to generate the list of commands available on the command line. For example, since the folder `/bin` is typically on the path, putting an executable program in that folder will make it available as a command.


