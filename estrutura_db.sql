clientes:
  id (UUID, PRIMARY KEY)
  nome (TEXT, UNIQUE, NOT NULL)
  created_at (TIMESTAMPTZ)
  updated_at (TIMESTAMPTZ)

veeam_hosts:
  id (UUID, PRIMARY KEY)
  id_cliente (UUID, FOREIGN KEY clientes(id))
  apelido (TEXT, NOT NULL)
  acesso_com (TEXT) -- RDP_LOCAL/RDP_EXTERNO/ANYDESK/SSH
  ip_interno (INET)
  ip_externo (INET)
  descricao (TEXT)
  veeam_version (TEXT) -- Versão do Veeam
  last_seen (TIMESTAMPTZ) -- Última vez que reportou
  created_at (TIMESTAMPTZ)
  updated_at (TIMESTAMPTZ)

veeam_jobs:
  id (UUID, PRIMARY KEY) -- (Get-VBRJob | ConvertTo-Json).Info.Id
  id_cliente (UUID, FOREIGN KEY clientes(id))
  id_host (UUID, FOREIGN KEY veeam_hosts(id))
  apelido (TEXT, NOT NULL) -- (Get-VBRJob | ConvertTo-Json).Info.Name
  description (TEXT)
  schedule_enabled (BOOLEAN)
  created_at (TIMESTAMPTZ)
  updated_at (TIMESTAMPTZ)

job_reports:
  id (UUID, PRIMARY KEY)
  id_cliente (UUID, FOREIGN KEY clientes(id))
  id_job (UUID, FOREIGN KEY veeam_jobs(id))
  id_host (UUID, FOREIGN KEY veeam_hosts(id))
  status (TEXT) -- Success/Warning/Failed/Running
  session_id (TEXT) -- Session ID único do Veeam
  start_time (TIMESTAMPTZ) -- Início do job
  end_time (TIMESTAMPTZ) -- Término do job
  created_at (TIMESTAMPTZ)