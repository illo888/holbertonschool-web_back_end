# NoSQL

This project explores NoSQL databases, specifically MongoDB, covering database operations, document queries, and Python integration with PyMongo.

## Learning Objectives

- Understand NoSQL concepts and differences from SQL
- Work with document storage and MongoDB operations
- Query, insert, update, and delete documents
- Use PyMongo for Python-MongoDB integration
- Perform aggregation and data analysis

## Requirements

### MongoDB Command Files
- Ubuntu 20.04 LTS
- MongoDB version 4.4
- All files end with a new line
- First line must be a comment: `// my comment`

### Python Scripts
- Python 3.9
- PyMongo 4.8.0
- pycodestyle 2.5.*
- All files executable and end with `#!/usr/bin/env python3`
- Complete module and function documentation
- Type annotations where applicable

## Files

### MongoDB Shell Scripts
- `0-list_databases` - List all databases
- `1-use_or_create_database` - Create or use a database
- `2-insert` - Insert a document into a collection
- `3-all` - List all documents in a collection
- `4-match` - List documents matching criteria
- `5-count` - Count documents in a collection
- `6-update` - Update documents
- `7-delete` - Delete documents matching criteria
- `100-find` - Query with regex filter

### Python Scripts
- `8-all.py` - List all documents using PyMongo
- `9-insert_school.py` - Insert document with kwargs
- `10-update_topics.py` - Update school topics
- `11-schools_by_topic.py` - Find schools by topic
- `12-log_stats.py` - Nginx log statistics
- `101-students.py` - Sort students by average score
- `102-log_stats.py` - Enhanced log stats with top IPs

## Usage

Run MongoDB scripts:
```bash
cat 0-list_databases | mongo
cat 2-insert | mongo my_db
```

Run Python scripts:
```bash
./8-main.py
./12-log_stats.py
```
