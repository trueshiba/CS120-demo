#include <iostream>
#include <iomanip>
#include <sstream>
#include <chrono>

int main()
{
    //No longer a string - Mish
    std::string date_str = 2022-03-17 10:45:30;
    std::tm date_obj = {};
    //Change variable name -Mish
    std::istringstream ss(date_sr);
    //No semicolon - Mish
    ss >> std::get_time(&date_obj, "%Y-%m-%d %H:%M:%S")
    std::stringstream formatted_date_ss;
    formatted_date_ss << std::put_time(&date_obj, "%m/%d/%Y %H:%M:%S");
    //No Semicolon - Mish
    std::string formatted_date = formatted_date_ss.str()

    std::cout << formatted_date << std::endl;
    
    //Mish was double here! HA

    return 0;
}
