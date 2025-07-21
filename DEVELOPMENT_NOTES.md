# Development Notes

## Git Learning Outcomes

### Commands Mastered:
- `git init` - Initialize repository
- `git status` - Check repository status
- `git add` - Stage changes
- `git commit` - Save changes
- `git log` - View history
- `git diff` - See changes
- `git reset` - Undo operations
- `git checkout` - Switch branches/restore files

### Best Practices Learned:
1. **Commit Messages**: Use clear, descriptive messages
2. **Frequent Commits**: Small, logical commits are better
3. **Staging**: Review changes before committing
4. **Documentation**: Always include README and comments

### Git Workflow:

Make changes
git status (check what changed)
git add (stage changes)
git status (verify staging)
git commit (save with message)
git push (share with others)


## Project Architecture

### Current Structure:
python-task-manager/
├── app.py              # Main Flask application
├── utils.py            # Helper functions
├── test_api.py         # API testing script
├── requirements.txt    # Dependencies
├── .gitignore         # Git ignore rules
├── README.md          # Project documentation
└── DEVELOPMENT_NOTES.md # Learning notes

### API Design Decisions:
- RESTful endpoints for CRUD operations
- JSON-only communication
- In-memory storage for simplicity
- Proper HTTP status codes
- Error handling with meaningful messages

## Next Steps for Day 2:
1. Database integration (SQLite)
2. Data persistence
3. Advanced Git branching
4. Pull requests workflow
5. Deployment preparation