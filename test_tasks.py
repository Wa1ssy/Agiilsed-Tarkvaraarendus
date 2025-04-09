     
     
     def test_mark_done():
         task = Task("Testi ülesanne")
         task.mark_done()
         assert.tast_status == "done"