## 🌀 Generate a Super Cool GitHub Contribution Graph

Follow these steps to create and showcase an awesome contribution graph on your GitHub profile:

### 📥 Step 1: Download the Repository
Clone this repository to your local machine:

```bash
git clone git@github.com:cu8code/super-cool-github-graph-generator.git
```

### 🛠️ Step 2: Run the Script
Navigate into the project directory and run the script to generate the desired commit history:

```bash
cd super-cool-github-graph-generator
python3 create_commit.py
```

> **Note**: Replace `script_name.sh` with the actual script name provided in this repository.

### 🗑️ Step 3: Reset Git History
Remove the current `.git` directory to reset the repository:

```bash
rm -rf .git
```

### 🔄 Step 4: Reinitialize Git
Reinitialize the Git repository:

```bash
git init
git add .
git commit -m "Initial commit for contribution graph"
```

### ☁️ Step 5: Upload to GitHub
Push the updated repository to a new GitHub repository:

```bash
git remote add origin <new-repo-url>
git branch -M main
git push -u origin main
```
