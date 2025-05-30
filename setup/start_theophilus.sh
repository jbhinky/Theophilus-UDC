#!/bin/bash

echo "🚀 Initializing Theophilus Stage 1 Environment..."

# Step 1: Set up Python virtual environment
python3 -m venv theo_env
source theo_env/bin/activate

# Step 2: Install dependencies (if requirements.txt is present)
if [ -f requirements.txt ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found. Skipping dependency installation."
fi

# Step 3: Optional stimulus injection
echo ""
read -p "Would you like to generate sample stimuli? (y/n): " gen_stim
if [ "$gen_stim" = "y" ]; then
    echo "Generating sample stimuli..."
    python stimuli_builder.py --inputs "What are you?" "Why do you exist?" "I hear a sound"
    cp stimuli_built.json stimuli_example.json
    echo "✓ Stimuli written to stimuli_example.json"
fi

# Step 4: Run Theophilus
echo ""
read -p "Do you want to run Theophilus now? (y/n): " run_theo
if [ "$run_theo" = "y" ]; then
    echo "⚙️ Starting Theophilus..."
    python run_theophilus.py
else
    echo "You can start Theophilus later with: python run_theophilus.py"
fi
