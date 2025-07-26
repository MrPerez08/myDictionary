cmake_minimum_required(VERSION 3.10)
project(SpellChecker LANGUAGES CXX)

# Find Hunspell package
find_package(Hunspell REQUIRED)

# Add executable
add_executable(spellchecker src/main.cpp)

# Link Hunspell
target_link_libraries(spellchecker PRIVATE Hunspell::Hunspell)

# C++ standard
set_target_properties(spellchecker PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED ON
)

# Install dictionary files (optional)
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/dicts")
    file(GLOB DICT_FILES "dicts/*")
    install(FILES ${DICT_FILES} DESTINATION share/dicts)
endif()