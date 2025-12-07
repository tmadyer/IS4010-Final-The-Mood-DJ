import pytest
from unittest.mock import patch
import pandas as pd
from io import StringIO
import sys



from src import main

@patch('sys.stdout', new_callable=StringIO)
def test_main_dev_mode(mock_stdout):
    """
    Tests the main CLI function in dev mode.
    """
    # Mock command line arguments
    with patch.object(sys, 'argv', ['src/main.py', '--image-path', 'dummy.jpg', '--dev-mode']):
        # Mock logic functions
        with patch('src.logic.analyze_emotion', return_value='happy') as mock_analyze, \
             patch('src.logic.get_playlist', return_value=pd.DataFrame({
                 'track_name': ['Test Track'],
                 'artist_name': ['Test Artist'],
                 'album_name': ['Test Album']
             })) as mock_get_playlist:
            
            main.main()

            # Check that logic functions were called correctly
            mock_analyze.assert_called_once_with('dummy.jpg', dev_mode=True)
            mock_get_playlist.assert_called_once_with('happy')

            # Check the output
            output = mock_stdout.getvalue()
            assert "Analyzing your mood..." in output
            assert "We think you're feeling: Happy" in output
            assert "Generating your playlist..." in output
            assert "Test Track" in output

@patch('sys.stdout', new_callable=StringIO)
def test_main_help(mock_stdout):
    """
    Tests the main CLI function with the --help argument.
    """
    with pytest.raises(SystemExit) as e:
        with patch.object(sys, 'argv', ['src/main.py', '--help']):
            main.main()
    
    # Check that the exit code is 0
    assert e.type == SystemExit
    assert e.value.code == 0

    # Check that the output contains usage information
    output = mock_stdout.getvalue()
    assert "usage: main.py [-h]" in output
    assert "Analyzes your mood from a picture and suggests a playlist." in output
