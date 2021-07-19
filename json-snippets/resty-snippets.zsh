if [[ $SHELL != $(which zsh) ]]; then
	echo "these snippets are only tested in zsh"
else
	resty "http://localhost:8088"

	this_dir="$(dirname $0)"

	unalias GET &>/dev/null
	unset -f GET &>/dev/null
	function GET() {
		# "$@" will be covnerted to @$ when this file is sourced
		# 	so the function will actually run with $@
		#	which expands to all arguments given to the function itself
		resty-get "$@" | jq .
	}

	unset -f POST_animal &>/dev/null
	function POST_animal() {
		resty-post -V <${this_dir}/animal.json
	}
	unset -f PUT_animal &>/dev/null
	function PUT_animal() {
		if [[ $# -eq 0 ]]; then
			echo provide an id
		else
			echo $(resty-get /animals/$1) | jq . | resty-put -V
		fi
	}

	unset -f POST_employee &>/dev/null
	function POST_employee() {
		resty-post -V <${this_dir}/employee.json
	}
	unset -f PUT_employee &>/dev/null
	function PUT_employee() {
		if [[ $# -eq 0 ]]; then
			echo provide an id
		else
			echo $(resty-get /employees/$1) | jq . | resty-put -V
		fi
	}

	unset -f POST_customer &>/dev/null
	function POST_customer() {
		resty-post -V <${this_dir}/customer.json
	}
	unset -f PUT_customer &>/dev/null
	function PUT_customer() {
		if [[ $# -eq 0 ]]; then
			echo provide an id
		else
			echo $(resty-get /customers/$1) | jq . | resty-put -V
		fi
	}

	unset -f POST_location &>/dev/null
	function POST_location() {
		resty-post -V <${this_dir}/location.json
	}
	unset -f PUT_location &>/dev/null
	function PUT_location() {
		if [[ $# -eq 0 ]]; then
			echo provide an id
		else
			echo $(resty-get /locations/$1) | jq . | resty-put -V
		fi
	}
fi

### you'll need this
#
# unalias $(alias | grep POST_ | cut -d "=" -f 1)
#
