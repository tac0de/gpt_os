from system.os_manager import OSManager

def test_full_command_flow():
    os = OSManager()

    # Step 1: Remember something
    result1 = os.handle_command("remember lang Python")
    assert "lang → Python" in result1

    # Step 2: Query the remembered value
    result2 = os.handle_command("query lang")
    assert "Python" in result2

    # Step 3: Summarize the memory
    result3 = os.handle_command("summarize")
    assert "lang → Python" in result3

    # Step 4: Delete the memory
    result4 = os.handle_command("delete lang")
    assert "Deleted lang" in result4

    # Step 5: Query again (should be gone)
    result5 = os.handle_command("query lang")
    assert "No memory found" in result5 or result5.strip() == "[QUERY] \n"

    # Step 6: Export log (at least something should be there)
    result6 = os.handle_command("exportlog")
    assert "[LOG]" in result6
    assert "remember lang" in result6
