vertex_simple = \
    '''
    #version 120
    attribute vec3 vertex_pos;

    uniform mat4 MVP;

    void main() {
        gl_Position = MVP * vec4(vertex_pos, 1.0);
    }
    '''

fragment_simple = \
    '''
    void main(void)
    {
      gl_FragColor = vec4(0.3, 0.3, 0.5, 1.0);
    }
    '''

vertex_shaded = \
    '''
    #version 120
    attribute vec3 vertex_pos_model_space;
        attribute vec3 vertex_normal_model_space;

    varying vec3 pos_world_space;
    varying vec3 normal_camera_space;
    varying vec3 eye_direction_camera_space;
    varying vec3 light_direction_camera_space;

    uniform mat4 MVP;
    uniform mat4 V;
    uniform mat4 M;
    uniform vec3 light_pos_world_space;

    void main() {

        // Output position of the vertex, in clip space : MVP * position
        gl_Position =  MVP * vec4(vertex_pos_model_space, 1.0);

        // Position of the vertex, in worldspace : M * position
        pos_world_space = (M * vec4(vertex_pos_model_space, 1)).xyz;

        // Vector that goes from the vertex to the camera, in camera space.
        // In camera space, the camera is at the origin (0,0,0).
        vec3 vertex_pos_camera_space = (V * M * vec4(vertex_pos_model_space, 1.0)).xyz;
        eye_direction_camera_space = vec3(0.0, 0.0, 0.0) - vertex_pos_camera_space;

        // Vector that goes from the vertex to the light, in camera space. M is omitted because it's identity.
        vec3 light_pos_camera_space = (V * M * vec4(light_pos_world_space, 1.0)).xyz;
        light_direction_camera_space = light_pos_camera_space + eye_direction_camera_space;

        // Normal of the the vertex, in camera space
        normal_camera_space = (V * M * vec4(vertex_normal_model_space, 0.0)).xyz; // Only correct if ModelMatrix does not scale the model ! Use its inverse transpose if not.
    }
    '''

fragment_shaded = \
    '''
    #version 120

    // Interpolated values from the vertex shaders
    varying vec3 pos_world_space;
    varying vec3 normal_camera_space;
    varying vec3 eye_direction_camera_space;
    varying vec3 light_direction_camera_space;

    // Values that stay constant for the whole mesh.
    uniform vec3 color;
    uniform vec3 light_pos_world_space;

    void main() {

        // Light emission properties
        // You probably want to put them as uniforms
        vec3 LightColor = vec3(1, 1, 1);
        float LightPower = 100.0f;

        // Material properties
        vec3 MaterialDiffuseColor = color;
        vec3 MaterialAmbientColor = vec3(0.1, 0.1, 0.1) * MaterialDiffuseColor;
        vec3 MaterialSpecularColor = vec3(0.3, 0.3, 0.3);

        // Distance to the light
        float distance = length(light_pos_world_space - pos_world_space);

        // Normal of the computed fragment, in camera space
        vec3 n = normalize(normal_camera_space);
        // Direction of the light (from the fragment to the light)
        vec3 l = normalize(light_direction_camera_space);
        // Cosine of the angle between the normal and the light direction,
        // clamped above 0
        //  - light is at the vertical of the triangle -> 1
        //  - light is perpendicular to the triangle -> 0
        //  - light is behind the triangle -> 0
        float cosTheta = clamp(dot(n, l), 0, 1);

        // Eye vector (towards the camera)
        vec3 E = normalize(eye_direction_camera_space);
        // Direction in which the triangle reflects the light
        vec3 R = reflect(-l,n);
        // Cosine of the angle between the Eye vector and the Reflect vector,
        // clamped to 0
        //  - Looking into the reflection -> 1
        //  - Looking elsewhere -> < 1
        float cosAlpha = clamp(dot(E, R), 0, 1);

        gl_FragColor.rgb =
            // Ambient : simulates indirect lighting
            MaterialAmbientColor +
            // Diffuse : "color" of the object
            MaterialDiffuseColor * LightColor * LightPower * cosTheta / (distance*distance) +
            // Specular : reflective highlight, like a mirror
            MaterialSpecularColor * LightColor * LightPower * pow(cosAlpha,5) / (distance*distance);
        }
    '''