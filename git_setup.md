# Pushing Your Code to GitHub

Follow these steps to push your newsletter signup application to GitHub:

## 1. Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right and select "New repository"
3. Name your repository (e.g., "newsletter-signup")
4. Keep it "Public" or make it "Private" based on your preference
5. Don't initialize with README (we already have one)
6. Click "Create repository"

## 2. Initialize Git Repository Locally

Open your terminal and navigate to the newsletter-signup directory:

```bash
cd /Users/vlad.scanteie/Sites/localhost/newsletter-signup
```

Initialize a new Git repository:

```bash
git init
```

## 3. Add Your Files

Stage all your files for commit:

```bash
git add .
```

You can verify what will be committed:

```bash
git status
```

## 4. Make Your First Commit

Commit your files with a descriptive message:

```bash
git commit -m "Initial commit: Newsletter signup application"
```

## 5. Link to GitHub Repository

Replace `YOUR_USERNAME` with your GitHub username and `REPO_NAME` with your repository name:

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

## 6. Push Your Code

Push your code to GitHub:

```bash
git push -u origin main
```

If your default branch is "master" instead of "main", use:

```bash
git push -u origin master
```

## 7. Verify

1. Go to your GitHub repository page
2. Refresh the page
3. You should see all your files there

## Common Issues and Solutions

1. **If you get "fatal: remote origin already exists"**:
   ```bash
   git remote remove origin
   ```
   Then try adding the remote again.

2. **If you need to update your code later**:
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push
   ```

3. **If push is rejected**:
   ```bash
   git pull origin main
   ```
   Resolve any conflicts, then try pushing again.

## Best Practices

1. Always check `git status` before committing
2. Write clear commit messages
3. Pull before pushing if working with others
4. Keep sensitive data out of Git (already handled by .gitignore)

## Next Steps

After successfully pushing your code to GitHub, you can:

1. Follow the deployment guide in deployment.md
2. Set up branch protection rules in GitHub
3. Enable GitHub Actions for CI/CD
4. Add collaborators if working with a team

Remember to never commit sensitive information like passwords or API keys. Use environment variables for those as described in the deployment guide.