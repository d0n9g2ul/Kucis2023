import argparse
import os
import pyExtract.extract

root_directory_path = os.path.dirname(os.path.abspath(__file__))

def create_main_directory(root_directory_path):
    if not os.path.exists(root_directory_path+"/result"):
        os.makedirs(root_directory_path+"/result")
        print("Created result directory: ", root_directory_path + "/result")


def main():
    create_main_directory(root_directory_path)
    parser = argparse.ArgumentParser(description='exDG Log Analyzer Tool')
    subparsers = parser.add_subparsers(title='Subcommands', dest='subcommand')

    #All
    file_parser = subparsers.add_parser('all', help='Extract All information')

    # File Subparsers
    file_parser = subparsers.add_parser('file', help='Extract file information')
    
    file_subparsers = file_parser.add_subparsers(title='File Subcommands', dest='file_subcommand')

    modifytime_parser = file_subparsers.add_parser('modify', help='Extract file final modify time')
    modifytime_parser.add_argument('-d', '--directory', default='logs', help='Directory path(s) for extract')

    accesstime_parser = file_subparsers.add_parser('access', help='Extract file final access time')
    accesstime_parser.add_argument('-d', '--directory', default='logs', help='Directory path(s) for extract')

    birthtime_parser = file_subparsers.add_parser('birth', help='Extract file final birth time')
    birthtime_parser.add_argument('-d', '--directory', default='logs', help='Directory path(s) for extract')

    # Log Subparser
    log_parser = subparsers.add_parser('log', help='Extract log information')
    #log_parser.add_argument('-k', '--keyword', help='Keyword to search in logs')

    # System Subparser
    system_parser = subparsers.add_parser('system', help='Extract system information (netstat, pstree, top)')

    # Etc Subparser
    etc_parser = subparsers.add_parser('etc', help='Extract ETC information (history, login)')
    etc_subparser = etc_parser.add_subparsers(title='ETC subcommand', dest='etc_subcommand')
    etc_subparser.add_parser('hist', help="Extract History")
    etc_subparser.add_parser('last', help="Extract Login info (last, lastb)")
    
    args = parser.parse_args()

    if args.subcommand == "all":
        print("[***]\t All Extract \t[***]")
        pyExtract.extract.access_time(None)
        pyExtract.extract.modify_time(None)
        pyExtract.extract.birth_time(None)
        pyExtract.extract.log()
        pyExtract.extract.system()
        pyExtract.extract.history()
        pyExtract.extract.login()

    elif args.subcommand == 'file':
        if args.file_subcommand == 'modify':
            directory_path = args.directory if args.directory is not None else None
            pyExtract.extract.modify_time(directory_path)
            
        elif args.file_subcommand == 'access':
            directory_path = args.directory if args.directory is not None else None
            pyExtract.extract.access_time(directory_path)
            
        elif args.file_subcommand == 'birth':
            directory_path = args.directory if args.directory is not None else None
            pyExtract.extract.birth_time(directory_path)

    elif args.subcommand == 'log':
        pyExtract.extract.log()
    elif args.subcommand == 'system':
        pyExtract.extract.system()

    elif args.subcommand == 'etc':
        if args.etc_subcommand == "last":
            pyExtract.extract.login()

        elif args.etc_subcommand == "hist":
            pyExtract.extract.history()

        else:
            pyExtract.extract.history()
            pyExtract.extract.login()

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
