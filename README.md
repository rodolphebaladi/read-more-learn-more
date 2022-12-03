# read-more-learn-more

Clone Git repository used for implementation and test (requires *GITHUB_USERNAME*):
```
git clone git@github.com:<GITHUB_USERNAME>/read-more-learn-more.git
```

Clone Gerrit repository used for code reviews with Gerrit commit-msg hook script (requires *GERRITHUB_USERNAME*): 
```
git clone "ssh://<GERRITHUB_USERNAME>@review.gerrithub.io:29418/rodolphebaladi/read-more-learn-more" && scp -p -P 29418 <GERRITHUB_USERNAME>@review.gerrithub.io:hooks/commit-msg "read-more-learn-more/.git/hooks/"
```

Install application dependencies:
```
make setup
```

Compile and run the application:
```
make
```

Run application unit tests:
```
make unit-tests
```

Run application integration tests:
```
make integration-tests
```

Run application performance tests:
```
make performance-tests
```

Push committed changes and request code review on GerritHub:
```
git push origin HEAD:refs/for/<branch_name>
```
