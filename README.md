Command Line Utility to fetch webpages
=========

Task
----

Please implement a command line program that can fetch web pages and saves them to disk for later retrieval and browsing.

##### Section 1

For example if we invoked your program like this: `./fetch [https://www.google.com](https://www.google.com)` then in our current directory we should have a file containing the contents of `www.google.com`. (i.e. `/home/myusername/fetch/www.google.com.html`).

We should be able to specify as many urls as we want:

```
$> ./fetch https://www.google.com https://autify.com <...>
$> ls
autify.com.html www.google.com.html
```

If the program runs into any errors while downloading the html it should print the error to the console.

##### Section 2

Record metadata about what was fetched:

- What was date and time of last fetch
- How many links are on the page
- How many images are on the page

Modify the script to print this metadata.

For example (it can work differently if you like)

```
$> ./fetch --metadata https://www.google.com
site: www.google.com
num_links: 35
images: 3
last_fetch: Tue Mar 16 2021 15:46 UTC
```

Code structure
----
The Code structure is explained as follows:

- main.py - Main entry file of the utlity.
- Utils - Directory contains the helpers.py and enums.py. Helpers contains all the common modules of the utlity. Enums contains the enums required across the appplication.
- Handles - Handles contains all the different functionality provided by the utiliy like saving webpages and getting metadata.

Details
----

#### Steps to run

- pipenv install
- pipenv run python main.py https://www.google.com https://duckduckgo.com
