#!/usr/bin/env python3
"""
Run all seeding scripts in sequence
"""

import subprocess
import sys
import time

def run_script(script_name):
    """Run a seeding script and measure time"""
    print(f"\n{'='*50}")
    print(f"🚀 Running {script_name}...")
    print(f"{'='*50}")
    
    start_time = time.time()
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, 
                              text=True, 
                              check=True)
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(result.stdout)
        print(f"✅ {script_name} completed in {duration:.2f} seconds")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ {script_name} failed:")
        print(f"Exit code: {e.returncode}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    """Run all seeding scripts in order"""
    print("🌱 Starting complete database seeding...")
    
    scripts = [
        'seed_theaters.py',
        'seed_movies.py', 
        'seed_shows.py'
    ]
    
    total_start = time.time()
    
    for script in scripts:
        success = run_script(script)
        if not success:
            print(f"\n❌ Seeding failed at {script}")
            return
    
    total_end = time.time()
    total_duration = total_end - total_start
    
    print(f"\n{'='*50}")
    print(f"🎉 All seeding completed successfully!")
    print(f"⏱️  Total time: {total_duration:.2f} seconds")
    print(f"{'='*50}")
    print(f"\n🚀 Your movie booking system is ready!")
    print(f"   Frontend: http://localhost:5173")
    print(f"   Backend API: http://localhost:5000/api")

if __name__ == '__main__':
    main()
