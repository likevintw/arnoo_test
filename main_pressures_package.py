
import request_structure
import arnno_test_handler

# python3 -m unittest -v

ARNOO_URL = 'http://test-agent.arnoo.com/aims'
AI_ID = {
    "human": "3126a0df-bbe8-4e80-b1f2-e7ff9c8dcff6",
    "flame": "640d3f58-5d67-43b6-8864-63753f4934a2",
    "pet": "2a96965c-b2f6-4850-a046-71fc952dee9e",
    "package": "b23301a7-f523-4dac-8574-10522dba21b0"
}
IMAGE_URL = {
    "flame": "http://192.168.5.130/upload/flame1.jpg",
    "human": "http://192.168.5.130/upload/human1.jpg",
    "pet": "http://192.168.5.130/upload/pet1.jpg",
    "package": "http://192.168.5.130/upload/package1.jpg"
}


if __name__ == '__main__':
    project = "package"
    handler = arnno_test_handler.create_arnoo_tester(
        project_name="arnoo_agentv210_packagev029_pressure",
        url=ARNOO_URL,
        image_url="http://192.168.5.130/upload/package111.png",
        ai_id=AI_ID[project],
        thread_times=1,
        response_flag=True)
    structure = request_structure.AiTestStructure()
    structure.run_pressure_test(handler, 100)
    structure.run_pressure_test(handler, 500)
    structure.run_pressure_test(handler, 1000)
    structure.run_pressure_test(handler, 1200)
