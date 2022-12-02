# read-more-learn-more

Clone repository with Gerrit commit-msg hook script: 
```
git clone "ssh://rodolphebaladi@review.gerrithub.io:29418/rodolphebaladi/read-more-learn-more" && scp -p -P 29418 rodolphebaladi@review.gerrithub.io:hooks/commit-msg "read-more-learn-more/.git/hooks/"
```

Compile and run the application:
```
make
```

Run application unit tests:
```
make testing
```

Push committed changes and request code review on GerritHub.io:
```
git push origin HEAD:refs/for/<branch_name>
```

