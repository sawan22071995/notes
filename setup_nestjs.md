# My NestJS setup

project directory has the following directories

```bash
00_tools
01_scripts
04_notes
99_source
```

## Install nodejs

Download nodejs from <https://nodejs.org/en/download/>

unzip inside 00_tools

## prepare env.sh

Prepare env.sh at project root

```bash
$ touch env.sh
```

Contents of env.sh

```bash
#!/bin/bash

export NODE_HOME=/home/manohar/projects/office/<project_name>/00_tools/node-v12.16.3-linux-x64
export PATH=$PATH:$NODE_HOME/bin
```

## Install nest client

```bash
#cd to project root and then execute below commands
$ cd 00_tools
$ npm i @nestjs/cli

# now inside 00_tools you should see following files and directories
# node_modules, node-v12.16.3-linux-x64 and package-lock.json
```

## Add node modules to path

update env.sh under root directory with the below contents

```bash
#!/bin/bash

export NODE_HOME=/home/manohar/projects/office/<project_name>/00_tools/node-v12.16.3-linux-x64
export NODE_MODULES_HOME=/home/manohar/projects/office/<project_name>/00_tools/node_modules
export PATH=$PATH:$NODE_HOME/bin:$NODE_MODULES_HOME/.bin
```

## Source env.sh

```bash
$ . ./env.sh
```

## Create new nest project

```bash
$ nest new <project_name>
```

## Create startup scripts

Create a file start.sh inside 01_scripts with below contents

```bash
#!/bin/bash

. /home/manohar/projects/office/<proj_name>/env.sh
cd /home/manohar/projects/office/<proj_name>/99_source/user-management
npm run start
```

## Access application

Access app on http://localhost:3000/

## Troubleshooting

Cannot find module @nestjs/microservices

Solution - go inside 99_source/proj_name and do 

```bash
$ npm i --save @nestjs/microservices
```
