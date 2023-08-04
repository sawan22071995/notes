Steps to change bash prompt in Linux/ubuntu/Kubuntu
====================================================

1. Copy the following to ~/.bashrc at the end of the file
    ```bash
    {% raw %}
	function parse_git_branch () {
	  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
	}

	YELLOW="\033[00;38;5;011m\]"
	RED="\033[00;38;5;009m\]"
	GREEN="\033[00;38;5;010m\]"
	PURPLE="\033[00;38;5;013m\]"
	GREEN2="\033[00;38;5;087m\]"

	#RED="\[\033[1;31m\]"
	#YELLOW="\[\033[0;33m\]"
	GREEN="\[\033[1;32m\]"
	NO_COLOR="\[\033[0m\]"
	MAGENTA="\[\033[31m\]"
	ORANGE="\[\033[33m\]"
	#PURPLE="\[\033[35m\]"
	WHITE="\[\033[37m\]"
	BOLD=""
	RESET="\[\033[m\]"

	#PS1="$GREEN\u@\h$NO_COLOR:\w$YELLOW\$(parse_git_branch)$NO_COLOR\$ "
	PS1="$YELLOW\h | $PURPLE\D{%G %m %d} $WHITE| $MAGENTA\t $WHITE| $GREEN2\W $WHITE|$GREEN\$(parse_git_branch)$RESET \n$RED⚡ $RESET"
    {% endraw %}
    ```
2. source ~/.bashrc
3. with the above changes, prompt would look like this
    ```bash
    dell13 | 2021 05 15 | 15:07:13 | nextjs-blog | (feature-api-routes) 
    ⚡
    ```
    ![image](https://user-images.githubusercontent.com/2945080/140285264-a00d6583-1e90-4696-aec9-61f615f51fbc.png)



