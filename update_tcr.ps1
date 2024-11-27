# PowerShell Script to Run Python Script, Commit Changes to Git, and Push to Remote

# Set Execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Path to the Python script and Git repository
$pythonScriptPath = "C:\Users\Ralph\Desktop\TCR\TCR_build\main.py"
$repoPath = "C:\Users\Ralph\Desktop\TCR\TCR"

# Step 1: Run the Python script
Write-Output "Running the Python script..."
python $pythonScriptPath

# Step 2: Navigate to the Git repository directory
Set-Location -Path $repoPath

# Step 3: Check the Git status to see if there are any changes
Write-Output "Checking for changes in the repository..."
$gitStatus = git status --porcelain

if ($gitStatus -ne "") {
    # Step 4: Stage all changes
    Write-Output "Staging all changes..."
    git add .

    # Step 5: Commit the changes with a timestamped message
    $commitMessage = "Auto-update commit on $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    Write-Output "Committing changes with message: $commitMessage"
    git commit -m $commitMessage

    # Step 6: Push changes to the remote repository
    Write-Output "Pushing changes to the remote repository..."
    git push origin main
    Write-Output "Repository synced successfully!"
} else {
    Write-Output "No changes detected. Nothing to commit."
}
