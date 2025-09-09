#!/usr/bin/env python3
"""
Text File Processing Program with Error Handling Lab
==================================================

This program demonstrates file I/O operations by:
1. Creating an input file with sample text
2. Reading and processing the text content
3. Writing results to an output file
4. **NEW**: Error Handling Lab - Interactive filename input with comprehensive error handling

Requirements fulfilled:
- Reads from input.txt
- Counts words in the file
- Converts text to uppercase
- Writes processed content to output.txt
- Provides success feedback
- **Enhanced**: Interactive error handling lab for custom filenames
"""

import os
from pathlib import Path
import sys


def create_input_file():
    """Create input.txt with sample content (at least 5 lines)"""
    sample_content = """Welcome to the world of Python programming!
File processing is a fundamental skill in programming.
This program demonstrates reading, processing, and writing files.
Python makes file operations simple and intuitive.
Learning file I/O opens up many possibilities for data processing.
You can process log files, configuration files, and much more.
Keep practicing and you'll master these concepts quickly!"""
    
    try:
        with open('input.txt', 'w', encoding='utf-8') as file:
            file.write(sample_content)
        print("✓ Created input.txt with sample content")
        return True
    except IOError as e:
        print(f"❌ Error creating input file: {e}")
        return False


def read_and_process_file():
    """Read input.txt, process content, and return processed data"""
    try:
        # Read the input file
        with open('input.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        
        print("✓ Successfully read input.txt")
        
        # Process the content
        word_count = count_words(content)
        uppercase_content = content.upper()
        
        print(f"✓ Processed content: {word_count} words found")
        
        return {
            'original_content': content,
            'processed_content': uppercase_content,
            'word_count': word_count
        }
        
    except FileNotFoundError:
        print("❌ Error: input.txt not found!")
        return None
    except IOError as e:
        print(f"❌ Error reading input file: {e}")
        return None


def count_words(text):
    """Count the number of words in the given text"""
    # Split by whitespace and filter out empty strings
    words = [word.strip() for word in text.split() if word.strip()]
    return len(words)


def write_output_file(processed_data):
    """Write processed content and word count to output.txt"""
    try:
        with open('output.txt', 'w', encoding='utf-8') as file:
            # Write header
            file.write("=" * 50 + "\n")
            file.write("PROCESSED TEXT FILE OUTPUT\n")
            file.write("=" * 50 + "\n\n")
            
            # Write word count
            file.write(f"TOTAL WORD COUNT: {processed_data['word_count']}\n\n")
            
            # Write separator
            file.write("-" * 30 + "\n")
            file.write("UPPERCASE CONTENT:\n")
            file.write("-" * 30 + "\n\n")
            
            # Write processed content
            file.write(processed_data['processed_content'])
            
            # Write footer
            file.write("\n\n" + "=" * 50 + "\n")
            file.write("End of processed content\n")
            file.write("=" * 50)
        
        print("✓ Successfully created output.txt")
        return True
        
    except IOError as e:
        print(f"❌ Error writing output file: {e}")
        return False


def display_file_info():
    """Display information about the created files"""
    files_info = []
    
    for filename in ['input.txt', 'output.txt']:
        if os.path.exists(filename):
            file_path = Path(filename)
            size = file_path.stat().st_size
            files_info.append(f"  📄 {filename}: {size} bytes")
        else:
            files_info.append(f"  ❌ {filename}: Not found")
    
    print("\n📁 File Information:")
    for info in files_info:
        print(info)


# ==========================================
# 🧪 ERROR HANDLING LAB - NEW FEATURE
# ==========================================

def error_handling_lab():
    """
    Interactive error handling lab that demonstrates various file error scenarios.
    This function allows users to specify custom filenames and handles multiple error types.
    """
    print("\n🧪 ERROR HANDLING LAB")
    print("=" * 50)
    print("This lab demonstrates comprehensive error handling for file operations.")
    print("You'll be able to test various error scenarios interactively.\n")
    
    while True:
        print("🔍 Choose an option:")
        print("  1. Read a custom file (test error handling)")
        print("  2. Create a new file with custom content")
        print("  3. Display current directory contents")
        print("  4. Test permission errors (advanced)")
        print("  5. Return to main program")
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                test_file_reading()
            elif choice == '2':
                create_custom_file()
            elif choice == '3':
                show_directory_contents()
            elif choice == '4':
                test_permission_errors()
            elif choice == '5':
                print("🎯 Returning to main program...")
                break
            else:
                print("❌ Invalid choice. Please enter 1-5.")
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted by user (Ctrl+C)")
            break
        except Exception as e:
            print(f"❌ Unexpected error in menu: {e}")


def test_file_reading():
    """Test reading files with comprehensive error handling"""
    print("\n📖 FILE READING TEST")
    print("-" * 30)
    
    while True:
        try:
            filename = input("Enter filename to read (or 'back' to return): ").strip()
            
            if filename.lower() == 'back':
                return
            
            if not filename:
                print("⚠️  Filename cannot be empty. Please try again.")
                continue
            
            # Attempt to read the file
            print(f"\n🔄 Attempting to read '{filename}'...")
            
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Success case
            word_count = count_words(content)
            lines = len(content.splitlines())
            
            print(f"✅ SUCCESS! File read successfully:")
            print(f"   📊 Lines: {lines}")
            print(f"   📊 Words: {word_count}")
            print(f"   📊 Characters: {len(content)}")
            
            # Show preview
            preview_length = min(200, len(content))
            print(f"\n📄 Content preview (first {preview_length} chars):")
            print(f"   {repr(content[:preview_length])}")
            if len(content) > preview_length:
                print("   ...")
            
            return
            
        except FileNotFoundError:
            print(f"❌ ERROR: File '{filename}' not found!")
            print("   💡 Tip: Check if the filename is spelled correctly.")
            print("   💡 Tip: Use option 3 to see available files.")
            
        except PermissionError:
            print(f"❌ ERROR: Permission denied accessing '{filename}'!")
            print("   💡 Tip: You don't have permission to read this file.")
            print("   💡 Tip: Try running as administrator or check file permissions.")
            
        except UnicodeDecodeError as e:
            print(f"❌ ERROR: Cannot decode '{filename}' as text!")
            print(f"   📋 Details: {e}")
            print("   💡 Tip: This might be a binary file (image, executable, etc.)")
            print("   💡 Tip: Try opening it with appropriate software.")
            
        except IsADirectoryError:
            print(f"❌ ERROR: '{filename}' is a directory, not a file!")
            print("   💡 Tip: Specify a file name, not a folder name.")
            
        except OSError as e:
            print(f"❌ ERROR: Operating system error!")
            print(f"   📋 Details: {e}")
            print("   💡 Tip: The file might be locked or corrupted.")
            
        except Exception as e:
            print(f"❌ UNEXPECTED ERROR: {type(e).__name__}")
            print(f"   📋 Details: {e}")
            print("   💡 Tip: This is an unusual error. Please check your input.")
        
        # Ask if user wants to try again
        try_again = input("\n🔄 Would you like to try another filename? (y/n): ").strip().lower()
        if try_again not in ['y', 'yes']:
            break


def create_custom_file():
    """Create a new file with user-specified content"""
    print("\n📝 CREATE CUSTOM FILE")
    print("-" * 30)
    
    try:
        filename = input("Enter filename to create: ").strip()
        
        if not filename:
            print("❌ Filename cannot be empty.")
            return
        
        # Check if file already exists
        if os.path.exists(filename):
            overwrite = input(f"⚠️  File '{filename}' already exists. Overwrite? (y/n): ").strip().lower()
            if overwrite not in ['y', 'yes']:
                print("🚫 File creation cancelled.")
                return
        
        print("\n📝 Enter file content (press Enter on empty line to finish):")
        print("   💡 Tip: You can enter multiple lines of text.")
        
        content_lines = []
        while True:
            line = input()
            if line == "":
                break
            content_lines.append(line)
        
        if not content_lines:
            print("⚠️  No content entered. Creating empty file.")
        
        content = '\n'.join(content_lines)
        
        # Attempt to create the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        
        # Success feedback
        file_size = os.path.getsize(filename)
        word_count = count_words(content)
        
        print(f"\n✅ SUCCESS! Created '{filename}':")
        print(f"   📊 Size: {file_size} bytes")
        print(f"   📊 Lines: {len(content_lines)}")
        print(f"   📊 Words: {word_count}")
        
    except PermissionError:
        print(f"❌ ERROR: Permission denied creating '{filename}'!")
        print("   💡 Tip: You might not have write permission in this directory.")
        
    except OSError as e:
        print(f"❌ ERROR: Cannot create file '{filename}'!")
        print(f"   📋 Details: {e}")
        print("   💡 Tip: Check if the filename contains invalid characters.")
        
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {type(e).__name__}")
        print(f"   📋 Details: {e}")


def show_directory_contents():
    """Display contents of the current directory"""
    print("\n📁 CURRENT DIRECTORY CONTENTS")
    print("-" * 40)
    
    try:
        current_dir = os.getcwd()
        print(f"📍 Current directory: {current_dir}")
        
        items = os.listdir('.')
        
        if not items:
            print("   📭 Directory is empty")
            return
        
        # Separate files and directories
        files = []
        directories = []
        
        for item in items:
            if os.path.isfile(item):
                size = os.path.getsize(item)
                files.append((item, size))
            elif os.path.isdir(item):
                directories.append(item)
        
        # Display directories
        if directories:
            print(f"\n📁 Directories ({len(directories)}):")
            for directory in sorted(directories):
                print(f"   📁 {directory}/")
        
        # Display files
        if files:
            print(f"\n📄 Files ({len(files)}):")
            for filename, size in sorted(files):
                print(f"   📄 {filename} ({size} bytes)")
        
        total_files = len(files)
        total_dirs = len(directories)
        print(f"\n📊 Total: {total_files} files, {total_dirs} directories")
        
    except PermissionError:
        print("❌ ERROR: Permission denied accessing current directory!")
        
    except Exception as e:
        print(f"❌ ERROR: Cannot list directory contents!")
        print(f"   📋 Details: {e}")


def test_permission_errors():
    """Test permission-related errors (advanced feature)"""
    print("\n🔒 PERMISSION ERROR TEST")
    print("-" * 30)
    print("⚠️  This test attempts to access system files that might be restricted.")
    print("    You may see permission errors - this is expected and educational!")
    
    # Test files that commonly have permission restrictions
    test_files = []
    
    # Add system-specific test files based on the operating system
    if sys.platform.startswith('win'):
        test_files = [
            'C:\\Windows\\System32\\config\\SAM',  # Windows registry file
            'C:\\pagefile.sys',  # Windows page file
            'C:\\Windows\\System32\\drivers\\etc\\hosts'  # Often readable
        ]
    else:  # Unix-like systems (Linux, macOS)
        test_files = [
            '/etc/shadow',  # Shadow password file
            '/root/.bashrc',  # Root user's bash config
            '/etc/passwd'  # Often readable
        ]
    
    proceed = input("🚀 Proceed with permission tests? (y/n): ").strip().lower()
    if proceed not in ['y', 'yes']:
        print("🚫 Permission tests cancelled.")
        return
    
    print("\n🔍 Testing file access permissions...")
    
    for test_file in test_files:
        print(f"\n📋 Testing: {test_file}")
        
        try:
            with open(test_file, 'r') as f:
                content = f.read(100)  # Read only first 100 chars
            print(f"   ✅ SUCCESS: File is readable!")
            print(f"   📄 Preview: {repr(content[:50])}...")
            
        except FileNotFoundError:
            print(f"   ℹ️  File not found (this is normal on some systems)")
            
        except PermissionError:
            print(f"   🔒 PERMISSION DENIED (this demonstrates the error type)")
            
        except Exception as e:
            print(f"   ❌ Other error: {type(e).__name__}: {e}")
    
    print(f"\n🎓 Educational Summary:")
    print(f"   • FileNotFoundError: File doesn't exist")
    print(f"   • PermissionError: Insufficient access rights")
    print(f"   • Other errors: Various system-specific issues")


def main():
    """Main function to orchestrate the file processing workflow"""
    print("🔹 TEXT FILE PROCESSING PROGRAM")
    print("=" * 40)
    
    # Step 1: Create input file
    print("\n📝 Step 1: Creating input file...")
    if not create_input_file():
        return
    
    # Step 2: Read and process the file
    print("\n🔄 Step 2: Reading and processing file...")
    processed_data = read_and_process_file()
    if not processed_data:
        return
    
    # Step 3: Write output file
    print("\n💾 Step 3: Writing output file...")
    if not write_output_file(processed_data):
        return
    
    # Step 4: Display success message and file information
    print("\n" + "=" * 40)
    print("🎉 SUCCESS! File processing completed successfully!")
    print("=" * 40)
    
    display_file_info()
    
    # Display summary
    print(f"\n📊 Processing Summary:")
    print(f"  • Words processed: {processed_data['word_count']}")
    print(f"  • Text converted to uppercase: ✓")
    print(f"  • Output file created: output.txt")
    
    print("\n💡 You can now check the contents of both files:")
    print("   - input.txt (original content)")
    print("   - output.txt (processed content)")


# Additional utility functions for enhanced functionality
def preview_files():
    """Preview the contents of both input and output files"""
    print("\n👀 FILE PREVIEW:")
    print("-" * 40)
    
    # Preview input file
    if os.path.exists('input.txt'):
        print("📄 input.txt (first 100 characters):")
        try:
            with open('input.txt', 'r', encoding='utf-8') as file:
                preview = file.read(100)
                print(f"   {preview}...")
        except IOError:
            print("   ❌ Could not read file")
    
    print()
    
    # Preview output file
    if os.path.exists('output.txt'):
        print("📄 output.txt (first 150 characters):")
        try:
            with open('output.txt', 'r', encoding='utf-8') as file:
                preview = file.read(150)
                print(f"   {preview}...")
        except IOError:
            print("   ❌ Could not read file")


if __name__ == "__main__":
    # Run the main program
    main()
    
    # Optional: Show file previews
    preview_files()
    
    # NEW FEATURE: Launch Error Handling Lab
    print("\n" + "=" * 50)
    launch_lab = input("🧪 Would you like to try the Error Handling Lab? (y/n): ").strip().lower()
    if launch_lab in ['y', 'yes']:
        error_handling_lab()
    
    print("\n✨ Program execution completed!")
