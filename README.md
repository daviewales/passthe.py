# passthe.py
Quickly generate passwords using a master password, a random seed, and website name.

## Dependencies
- [Python 3](https://www.python.org/downloads/)

## Usage
### Setting up a random seed
Before running passthe.py, you need to create a random seed in your home directory.
It should be a plain text file filled with random characters — for instance, a very large random number.
(The more characters in the file, the less chance someone else will have of guessing your seed. I use a 1000 digit random number, but that is probably overkill.)
It should have the name `passthe.py.seed`.

To recap, at this point you should have a file full of random characters at the following path:

    ~/.passthe.py.seed

### Running passthe.py
Now that you have a seed in the right location, running passthe.py should be fairly simple.
First, make sure it is executable by running

    chmod +x passthe.py
    
Then run passthe.py in your terminal.

    ./passthe.py

If you don't want to make passthe.py executable, you can execute it using Python as follows:

    python3 passthe.py

Enter the name of the website at the first prompt.

Enter your password at the second prompt.

Wait a second or two for your password to be generated.

## Attribution

The idea for this program was taken from [Pass the Pie](https://launchpad.net/pass-the-pie), by Cafeinoz.
He is on [Launchpad](https://launchpad.net/~cafeinoz) and [Github](https://github.com/cafeinoz).
