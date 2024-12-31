# std::optional
```c++
#include <optional>

std::optional<std::string> ReadFileAsString(cibs std::string& filepath){
	std::ifstream steam(filepath)
	if(stream){
		std::string result;
		//read file
		stream.close();
		return result;
	}
	else{
		return {};
	}
}

int main(){
	std::optional<std::string> data = ReadFileAsString("data.txt");
	if(data){
		//exist
	}
	else{
		// does not exist
	}
}
```
```c++
	std::string value = data.value_or("String");
```