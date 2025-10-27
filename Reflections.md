# **Lab 5: Reflection**

**1\. Which issues were the easiest to fix, and which were the hardest? Why?**  
The easiest issues to fix were the stylistic ones from Flake8, like missing blank lines  or renaming functions to snake\_case , as they were simple text edits. The hardest was the "mutable default argument" , because it required understanding a non-obvious Python concept (how default arguments are shared) rather than just fixing a simple syntax error.

**2\. Did the static analysis tools report any false positives? If so, describe one example.**  
In this lab, the tools did not report any clear false positives; every issue was valid. For example, the global-statement warning  might seem unnecessary in a tiny script, but it correctly flagged a poor practice that becomes problematic in larger applications. All the security and bug warnings pointed to real, tangible problems.

**3\. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.**  
I would use "pre-commit hooks" to run Flake8 and Bandit locally before I'm even allowed to make a commit, catching errors early. Then, I'd set up a GitHub Actions (CI) workflow to automatically run all three tools (Pylint, Flake8, Bandit) on every pull request, which blocks merging any code that fails the quality and security checks.

**4\. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**  
The code is far more robust and less likely to crash due to fixes like input validation, using stock\_data.get(), and specifying except KeyError:. Readability improved significantly with consistent naming and formatting. Most importantly, removing eval() and fixing the file handling made the code more secure and reliable.