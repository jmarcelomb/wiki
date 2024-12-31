# Standards

## C++98

1. Deterministic Object Lifetime
2. RAII (Resource Acquisition Is Initialization)
	- https://youtu.be/7Qgd9B1KuMQ
3.  Templates 98
	```c++
	template<typename First, typename Second>
	struct Pair{
		First i;
		Second j;
	};
	```

## C++11
- `auto`
- ranged-for loops
	```c++
	std::vector<int> &vec;
	for(const auto &elem : vec){}
	```
- lambdas
	```c++
	std::vector<int> &vec;
	const auto count = std::count(begin(vec), end(vec),
								  [](int i){ return i < 3; }
						);
	```
- variadic templates
	```c++
	template<typename Func, typename ...T>
	void call(const Func &function, const T& ... param){
		function(param...);
	}
	```
- `unique_ptr`/`shared_ptr`
	```c++
	#include <memory>
	void allocate_memory(){
		std::unique_ptr<int> ptr(new int(5));
	} //ptr is destroyed, memory freed
	```
- `constexpr`
	```c++
	constexpr int get_value(){
		return 5 * 3;
	}
	constexpr auto value = get_value();
	
	int main(){
		std:array<int, value> values;
	}
	```

## C++14

- Bug Fixes from C++11
- `auto` - return type deduction → enables auto in function return type
- Generic Lambdas
	```c++
	template<typename T>
	void count_things_less_than_3(const T &vec, int value){
		const auto count = std::count(begin(vec), end(vec), [](const auto i){return i < 3;})
	}
	```
- Generalized Capture expression
	```c++
	template<typename T>
	void count_things_less_than_3(const T &vec, int value){
		const auto count = std::count(begin(vec), end(vec),
							[value=3](const auto i){return i < 3;})
	}
	```
- `make_unique`/`make_shared`
	```c++
	#include <memory>
	void allocate_memory(){
		auto ptr{std::make_unique<int>(5)};
	} //ptr is destroyed, memory freed
	```
- `constexpr` is more flexible, loops, branches, multiple return statments

## C++17
- Guaranteed Copy / Move Elision
	```c++
	#include <memory>
	
	auto factory(){
		return std::make_unique<int>();
	}
	
	int main()
	{
		auto widget = factory(); // No copies
	}
	```
- Beginning `constexpr` support in std library
- `constexpr` lambdas
- `std::string_view`
	```c++
	#include <string_view>
	constexpr std::string_view name = "Hello";
	```
- Class Template Argument Deduction
	```c++
	#include <array>
	std:array<int, 5> data{1,2,3,4,5}; //c++14
	std:array data{1,2,3,4,5}; //c++17
	```
- Fold expressions
	```c++
	template<typename ...T>
	auto add(const T& ...param){
		return (param + ...); 
	}
	 
	int main(){
		return add(1,2,5,4,5,6,7);
	}
	```
- Structured bindings
	```c++
	// Example 1
	std::pair<int, int> values{1, 2};
	auto [first, second] = values;

	// Example 2
	std::tupple<std::string, int> CreatePerson(){
	return { "Cherno", 24};
	}
	
	int main(){
		auto[name, age] = CreatePerson();
	}
	```
- if-init expressions
	```c++
	if(auto [first, second] = values; first > 5){}
	```