import { Component, signal } from '@angular/core';
import { MatSidenavModule } from '@angular/material/sidenav';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'fn-root',
  imports: [RouterOutlet, MatSidenavModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'financier';

  isSideNavOpen = signal<boolean>(false);

  toggleSideNav() {
    this.isSideNavOpen.update((currentStatus) => !currentStatus);
  }
}
