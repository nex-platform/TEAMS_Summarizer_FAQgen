---
config:
  layout: dagre
---
flowchart TB
    %% Frontend Components
    subgraph Frontend["Frontend"]
        A["Streamlit Web Interface"]
        B["File Upload"]
        C["Summary & FAQ Output"]
        D["Controls & Settings"]
    end

    %% Backend Processing
    subgraph Backend["Backend"]
        E["File Processor"]
        F["Transcript Cleaner"]
        G["Document Parser"]
        H["Text Chunker"]
        I["AI Processing"]
        J["OpenAI API"]
        K["Summary Generator"]
        L["FAQ Extractor"]
        M["Action Item Extractor"]
        N["Response Formatter"]
    end

    %% Output
    subgraph Output["Output"]
        O["Formatted Document"]
        P[".docx Download"]
        Q["Display in UI"]
    end

    %% Data Storage
    subgraph Data["Data"]
        R[".env Configuration"]
        S["Template Files"]
        T["temp_images/"]
        U["Logs"]
        U1["app.log - INFO+"]
        U2["error.log - ERROR+"]
    end

    %% Monitoring
    subgraph Monitoring["Monitoring"]
        V["Logging System"]
        W["Status Codes"]
        X["Custom Log Levels"]
    end

    %% Connections
    A -->|User Input| B
    A -->|Display| C
    A -->|User Interaction| D
    B -->|Uploaded Files| E
    E --> F
    E --> G
    F --> H
    G --> H
    H --> I
    I --> J
    I --> K
    I --> L
    I --> M
    K --> N
    L --> N
    M --> N
    N --> O
    O --> P
    O --> Q
    J -->|API Key| R
    N -->|Uses| S
    A -.->|Logs| U
    E -.->|Logs| U
    I -.->|Logs| U
    V -->|Writes| U
    W -->|200/500| V
    X -->|SUCCESS/INFO/ERROR| V
    E -->|Temporary Files| T