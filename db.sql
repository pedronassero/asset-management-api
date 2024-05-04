create table if not exists asset (
    id VARCHAR(8) PRIMARY KEY,
    userId VARCHAR(50),
    name VARCHAR(100),
    description TEXT,
    acquisitionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('CRITICAL', 'WARNING', 'HEALTHY') DEFAULT 'HEALTHY',
    value FLOAT,
    nextMaintenance DATE
);

create table if not exists assetDependency (
    id VARCHAR(8) PRIMARY KEY,
    assetId VARCHAR(8), 
    name TEXT, 
    description TEXT,
    status ENUM('CRITICAL', 'WARNING', 'HEALTHY') DEFAULT 'HEALTHY',
    value FLOAT,
    nextMaintenance DATE,
    FOREIGN KEY (assetId) REFERENCES asset(id)
);