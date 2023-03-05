# Quickstart
Put folder sync in root of your obsidian repo that folder structure will look like that
.
├── README.md
├── cooking
│   ├── recipe1
│   └── recipe2
├── philosophy
│   ├── cioran
│   └── taleb
└── sync
    ├── Makefile
    ├── requirements.txt
    └── sync.py

```
sudo apt update
sudo apt install python3 make python3-pip git
pip3 install virtualenv
make install
make sync
```

# Autosync
Add execution of script to your favourite scheduler e.g. cron, windows task scheduler etc. Remember to add HOME env variable, without it git command will fail

example of cron script
```

```
