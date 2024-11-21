import os
from datetime import datetime, timedelta
import random
import subprocess

def create_commits(start_date_str, end_date_str, min_commits=0, max_commits=2, high_activity_probability=0.3):
    """
    Create commits to README.md file between specified dates with variable frequency.
    
    Args:
        start_date_str (str): Start date in 'YYYY-MM-DD' format
        end_date_str (str): End date in 'YYYY-MM-DD' format
        min_commits (int): Minimum commits per day
        max_commits (int): Maximum commits per day
        high_activity_probability (float): Probability of a high-activity day (0-1)
    """
    # Convert string dates to datetime objects
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    # Ensure README.md exists
    if not os.path.exists('temp.md'):
        with open('temp.md', 'w') as f:
            f.write('# Activity Log\n\n')
    
    current_date = start_date
    
    while current_date <= end_date:
        # Determine if this is a high-activity day
        is_high_activity = random.random() < high_activity_probability
        
        if is_high_activity:
            # High activity days have more commits
            day_min_commits = max(min_commits, max_commits // 2)
            day_max_commits = max_commits * 2
        else:
            # Regular days use standard min/max
            day_min_commits = min_commits
            day_max_commits = max_commits
        
        # Generate commits for the day
        num_commits = random.randint(day_min_commits, day_max_commits)
        
        # Create a list of random times for the day
        times = []
        for _ in range(num_commits):
            # Generate random hour and minute for the commit
            hour = random.randint(9, 18)  # Between 9 AM and 6 PM
            minute = random.randint(0, 59)
            times.append((hour, minute))
        
        # Sort times to make commits chronological
        times.sort()
        
        for hour, minute in times:
            # Create timestamp for commit
            timestamp = current_date.replace(hour=hour, minute=minute)
            
            # Generate a more varied commit message
            activity_types = [
                "Update documentation",
                "Add new section",
                "Fix typo",
                "Improve formatting",
                "Add content",
                "Update status",
                "Revise section",
                "Restructure document"
            ]
            
            # Update README with current timestamp and activity
            activity = random.choice(activity_types)
            with open('temp.md', 'a') as f:
                f.write(f'{activity}: {timestamp.strftime("%Y-%m-%d %H:%M")}\n')
            
            # Stage the changes
            subprocess.run(['git', 'add', 'temp.md'])
            
            # Create commit with custom date
            commit_env = os.environ.copy()
            commit_env['GIT_AUTHOR_DATE'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
            commit_env['GIT_COMMITTER_DATE'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
            
            commit_message = f"{activity} - {timestamp.strftime('%Y-%m-%d %H:%M')}"
            subprocess.run(['git', 'commit', '-m', commit_message], env=commit_env)
            
        current_date += timedelta(days=1)
    
    print(f"Created commits between {start_date_str} and {end_date_str}")
    print(f"Settings used:")
    print(f"- Minimum commits per day: {min_commits}")
    print(f"- Maximum commits per day: {max_commits}")
    print(f"- High activity day probability: {high_activity_probability * 100}%")
    print(f"- High activity day max commits: {max_commits * 2}")

if __name__ == "__main__":
    # Get date inputs from user
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    min_commits = int(input("Enter minimum commits per day (default 0): ") or "0")
    max_commits = int(input("Enter maximum commits per day (default 5): ") or "5")
    high_activity = float(input("Enter probability of high-activity days (0-1, default 0.3): ") or "0.3")
    
    try:
        create_commits(start_date, end_date, min_commits, max_commits, high_activity)
    except ValueError as e:
        print(f"Error: {e}")
        print("Please ensure dates are in YYYY-MM-DD format and numbers are valid")
