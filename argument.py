import sys
if __name__ == '__main__':
    if len(sys.argv)<2:
        print(f"Aucun argument apres le nom du script: {sys.argv[0]}")
    else:
        for i in range(1, len(sys.argv)):
            print(f'\t-->{sys.argv[i]}')
