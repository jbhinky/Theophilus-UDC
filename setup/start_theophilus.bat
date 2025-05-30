@echo off
echo ==========================================
echo   🚀 Theophilus Stage 1 Launcher (Windows)
echo ==========================================

:: Step 1: Set up virtual environment
echo Creating virtual environment...
python -m venv theo_env
call theo_env\Scripts\activate

:: Step 2: Install dependencies
IF EXIST requirements.txt (
    echo Installing dependencies...
    pip install -r requirements.txt
) ELSE (
    echo WARNING: requirements.txt not found. Skipping dependency installation.
)

:: Step 3: Optional stimulus input
set /P GENSTIM=Would you like to generate sample stimuli? (y/n): 
IF /I "%GENSTIM%"=="y" (
    echo Generating sample stimuli...
    python stimuli_builder.py --inputs "What are you?" "Why do you exist?" "I hear a sound"
    copy /Y stimuli_built.json stimuli_example.json
    echo Stimuli saved to stimuli_example.json
)

:: Step 4: Option to run
set /P RUNTHEO=Do you want to run Theophilus now? (y/n): 
IF /I "%RUNTHEO%"=="y" (
    echo Starting Theophilus...
    python run_theophilus.py
) ELSE (
    echo You can start Theophilus later with: python run_theophilus.py
)

pause
