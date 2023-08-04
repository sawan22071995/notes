# Typescript related

VS Code uses node only from /usr/bin/node. Even if you have NODE_HOME in PATH, it doesn't matter. When we run tsc:build or tsc:watch from command pallet of typescript, it will search for /usr/bin/node. if it is not there following error is thrown

``` bash
/usr/bin/env: ‘node’: No such file or directory
The terminal process terminated with exit code: 127
```

To fix this, we ended up creating soft link from node in custom directory to /usr/bin/node. But when project changes, it is important this is also changed. Usually I am maintaining this in project specific env.sh file

OR

You comment out creating soft link from env.sh. Make sure you source your env.sh from terminal and then fire VS Code from the same terminal



1st Tutorial followed - <https://www.youtube.com/watch?v=BLoFPda7fmI&list=PLhXZp00uXBk72m_G7E2Bshzd7PDpaInE1&index=1>



<https://www.youtube.com/watch?v=MdmLP7AG1FA&t=1484s>