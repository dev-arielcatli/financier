import { createServiceFactory, SpectatorService } from '@ngneat/spectator';
import { EndpointService } from './endpoint.service';
import { Endpoint } from './endpoint.model';
import { environment } from '../../../environments/environment';

describe('EndpointService', () => {
  let spectator: SpectatorService<EndpointService>;
  const createService = createServiceFactory(EndpointService);

  beforeEach(() => {
    spectator = createService();
  });
});
describe('EndpointService', () => {
  let spectator: SpectatorService<EndpointService>;
  const createService = createServiceFactory(EndpointService);

  beforeEach(() => {
    spectator = createService();
  });

  it('should create the service', () => {
    expect(spectator.service).toBeTruthy();
  });

  it('should build endpoint correctly', () => {
    const endpoint = 'api/expense/{expenseId}';
    const params = { expenseId: '123' };
    const builtEndpoint = spectator.service.buildEndpoint(endpoint, params);
    expect(builtEndpoint).toBe(`${environment.apiURL}/api/expense/123`);
  });
});
