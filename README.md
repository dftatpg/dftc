# git config --global user.name  Tomas
# git config --global user.email Tomas@163,com

# ssh-keygen -t rsa -C Tomas@163.com
# ssh-add ~/.ssh/id_rsa
# cat ~/.ssh/id_rsa.pub
# 

1. update master, create new branch in local
git checkout master
git pull
git checkout -b dev_xxx

2. git add xxx
   git rm  yyy

3. git status
   git diff

4. git commit -a 

5. before submit your code, you need rebase remote master, if got configlict, you have to solve the conflict !!
   git checkout dev_xxx
   git pull --rebase origin master

6. submit code:
   git push origin dev_xxx


7. delete merged branch
   git checkout master
   git branch -d dev_xxx

8. create another new branch to go-on development
   git checkout -b dev_yyy



# dftc
including some dft compile scripts
