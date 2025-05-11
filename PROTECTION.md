# Branch Protection Rules

## Summary

This repository uses **branch protection rules** for the `main` branch to ensure code quality, collaboration, and stability.

## Rules in Place

- ✅ **Pull Request Reviews Required**  
  At least one team member must approve changes before they can be merged into `main`.

- ✅ **Status Checks Required**  
  All commits must pass our CI checks (builds, tests, etc.) before being eligible for merge.

- ✅ **No Direct Pushes Allowed**  
  Direct pushes to the `main` branch are disabled. All changes must go through a pull request (PR).

## Why These Rules Matter

1. **Code Quality**  
   Reviews catch bugs early and ensure adherence to best practices.

2. **Collaboration**  
   Encourages team discussion and knowledge sharing around changes.

3. **Stability**  
   Prevents broken or untested code from reaching production.

4. **Auditability**  
   Every change is logged with an associated PR and review history.

5. **Security**  
   Reduces risk of accidental or unauthorized changes.
