document.addEventListener('DOMContentLoaded', function() {
      document.getElementById('definition').addEventListener('keyup', function(e) {
        if (e.key === 'Enter') {
          console.log('Working!');
        }
      });
    });