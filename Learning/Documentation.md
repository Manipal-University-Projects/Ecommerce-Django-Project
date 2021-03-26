# Git Commands

## Creating New branches

```
git checkout -b Login
git checkout -b Navbar
```

## For pushing from Local branches

```
git push --set-upstream origin Login
git push --set-upstream origin Navbar
```

## Merging

```
git checkout main
git merge Login
git merge Navbar
```

## Deleting the branches locally and remotely

```
git branch -d Login
git branch -d Navbar

git push origin --delete Login
git push origin --delete Navbar
```
## ALl Extensions

1. IntelliSense for CSS class names in HTML
