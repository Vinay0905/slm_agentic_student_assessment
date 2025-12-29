import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "slm-agentic-student-assessment"

list_of_files = [
    # Root files
    "README.md",
    ".gitignore",
    "docker-compose.yml",
    "Makefile",
    "LICENSE",
    
    # backend/
    "backend/app/main.py",
    "backend/app/api/v1/auth.py",
    "backend/app/api/v1/assessment.py",
    "backend/app/api/v1/results.py",
    "backend/app/api/v1/admin.py",
    
    # backend/app/agents/
    "backend/app/agents/orchestrator.py",
    "backend/app/agents/coding_agent.py",
    "backend/app/agents/aptitude_agent.py",
    "backend/app/agents/interview_agent.py",
    "backend/app/agents/supervisor_agent.py",
    "backend/app/agents/meta_scoring_agent.py",
    
    # backend/app/prompts/
    "backend/app/prompts/orchestrator.txt",
    "backend/app/prompts/coding_agent.txt",
    "backend/app/prompts/aptitude_agent.txt",
    "backend/app/prompts/interview_agent.txt",
    "backend/app/prompts/supervisor_agent.txt",
    "backend/app/prompts/meta_scoring_agent.txt",
    
    # backend/app/context/
    "backend/app/context/builder.py",
    "backend/app/context/contracts.py",
    "backend/app/context/filters.py",
    
    # backend/app/evaluation/
    "backend/app/evaluation/coding.py",
    "backend/app/evaluation/aptitude.py",
    "backend/app/evaluation/interview.py",
    "backend/app/evaluation/normalization.py",
    
    # backend/app/vector_db/
    "backend/app/vector_db/client.py",
    "backend/app/vector_db/embeddings.py",
    "backend/app/vector_db/retrieval.py",
    "backend/app/vector_db/plagiarism.py",
    
    # backend/app/models/
    "backend/app/models/student.py",
    "backend/app/models/assessment.py",
    "backend/app/models/evaluation.py",
    
    # backend/app/services/
    "backend/app/services/auth_service.py",
    "backend/app/services/assessment_service.py",
    "backend/app/services/scoring_service.py",
    "backend/app/services/ranking_service.py",
    
    # backend/app/storage/
    "backend/app/storage/db.py",
    "backend/app/storage/repositories/student_repo.py",
    "backend/app/storage/repositories/assessment_repo.py",
    
    # backend/app/utils/
    "backend/app/utils/logging.py",
    "backend/app/utils/metrics.py",
    "backend/app/utils/security.py",
    
    # backend/app/config/
    "backend/app/config/settings.py",
    "backend/app/config/constants.py",
    
    # backend/tests/
    "backend/tests/test_agents.py",
    "backend/tests/test_plagiarism.py",
    "backend/tests/test_ranking.py",
    
    "backend/requirements.txt",
    
    # frontend/
    "frontend/web/src/pages/.gitkeep",
    "frontend/web/src/components/.gitkeep",
    "frontend/web/src/services/.gitkeep",
    "frontend/web/src/hooks/.gitkeep",
    "frontend/web/public/.gitkeep",
    "frontend/web/package.json",
    
    "frontend/admin/src/.gitkeep",
    "frontend/admin/package.json",
    
    # infra/
    "infra/docker/backend.Dockerfile",
    "infra/docker/frontend.Dockerfile",
    "infra/k8s/backend.yaml",
    "infra/k8s/vector-db.yaml",
    
    # scripts/
    "scripts/seed_data.py",
    "scripts/run_local.sh",
    "scripts/evaluate_agents.py",
    
    # docs/
    "docs/architecture.md",
    "docs/context_engineering.md",
    "docs/flow_diagram.png"
]

base_path = Path(r"W:\Student_prediction_System")

# Create base directory if it doesn't exist
if not base_path.exists():
    base_path.mkdir(parents=True, exist_ok=True)
    logging.info(f"Created base directory: {base_path}")

for filepath in list_of_files:
    filepath = base_path / filepath
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not filepath.exists()) or (filepath.stat().st_size == 0):
        with open(filepath, "w") as f:
            pass  # Creates empty file
        logging.info(f"✅ Created empty file: {filepath}")
    else:
        logging.info(f"ℹ️  File already exists: {filepath}")

logging.info(f"🎉 Full-stack project structure '{project_name}' created successfully!")
logging.info(f"📁 Location: {base_path / project_name}")
logging.info(f"📊 Total files: {len(list_of_files)}")
