def backup_file(source_file, backup_file):
    source = open(source_file, 'r')
    data = source.read()
    source.close()

    backup = open(backup_file, 'w')
    backup.write(data)
    backup.close()

    print("Backup completed successfully!")

source = "file1.txt"
backup = "backup_file1.txt"
backup_file(source, backup)